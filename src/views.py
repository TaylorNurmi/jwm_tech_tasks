from flask import Blueprint, request, jsonify, render_template
from datetime import datetime
from models import Student
from __init__ import db
from pytz import UTC

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    return render_template('index.html')

@app_routes.route('/students', methods=['POST'])
def create_student():
    data = request.get_json() if request.is_json else request.form

    new_student = Student(
        name=data['name'], 
        birth_date=datetime.strptime(data['birth_date'], '%Y-%m-%d'),
        courses=data.get('courses', '')
    )

    db.session.add(new_student)
    db.session.commit()

    return jsonify({'id': new_student.id}), 201

@app_routes.route('/students', methods=['GET'])
def list_students():
    students = Student.query.all()
    student_list = [{'id': student.id, 'name': student.name, 'dob': student.birth_date, 'courses': student.courses} for student in students]
    return jsonify(student_list), 200

@app_routes.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get(id)
    if student:
        return jsonify({
            'id': student.id,
            'name': student.name,
            'birth_date': student.birth_date.strftime('%Y-%m-%d'),
            'courses': student.courses
        }), 200
    else:
        return jsonify({'message': 'Student not found'}), 404
    
@app_routes.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student deleted successfully'}), 200
    else:
        return jsonify({'message': 'Student not found'}), 404
    
@app_routes.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get(id)
    if student:
        data = request.get_json()
        
        if 'name' in data:
            student.name = data['name']
        if 'dob' in data:
            student.birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
        if 'courses' in data:
            student.courses = data['courses']
        
        student.updated_at = datetime.now(UTC)

        db.session.commit()
        return jsonify({
            'id': student.id,
            'name': student.name,
            'birth_date': student.birth_date.strftime('%Y-%m-%d'),
            'courses': student.courses
        }), 200
    else:
        return jsonify({'message': 'Student not found'}), 404
