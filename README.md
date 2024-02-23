Python Django Academic Project: Building a Student Complaint Box

**This project serves as an educational endeavor aimed at learning Python Django. It is developed within a virtual environment created in Visual Studio Code.**

Ensuring student satisfaction is paramount for any educational institution. However, often students encounter challenges in expressing their concerns or fail to access proper support from the organization. Grievances may encompass various forms of discontent, dissatisfaction, or negative perceptions, whether articulated or not. In today's context, addressing individual student issues or facilitating direct communication with specific staff members can be challenging. Grievance systems can be effectively managed by universities through their own websites.

SOFTWARE REQUIREMENTS

● Python
● Bootstrap 5
● Django
● HTML 5
● CSS3
● Mysql
● Visual Studio Code - Code Editor
● XAMPP

DATABASE DESIGN

● Table name: complaint_box_register
  Remark: to store user account details

● Table name: complaint_box_complaint
  Remark: to store student complaints

● Table name: complaint_box_faculty
  Remark: to store faculty details

● Table name: complaint_box_acknowledgement
  Remark: to store acknowledges from faculties

● Table name: complaint_box_facack
 Remark: to store acknowledges from admin to faculties

IMPLEMENTATION

The project have 3 modules: Student Module, Admin Module, Faculty Module

STUDENT MODULE

  1. Home page
  Home page consists of header,footer and services page. Header complaint
  register,login and home
  2. Register page
  Students can register a new account by entering the following details:
  Upload Image, User Name, User Email, Password and Phone Number. The
  entered data will be stored in the register table in the database.
  3. Login page
  Students can login to their account by entering user email and password to the
  login page
  4. Complaint page
  Students have choices to send complaints to the trainer,HR or Operations
  head. The complaint will be sent to the respective faculty.
  5. View acknowledgement page
  Students can view the acknowledgements for their complaints from this page
  6. View profile
  Details of the students can be seen in the user profile. Students can also edit
  their profile
  7. Logout
  Students can logout from their current account.
 

FACULTY MODULE
  1. Home page
  Home page consists of header,footer and services page. Header complaint
  register,login and home
  2. Login page
  Faculties can login to their account by entering designation,email and
  password.
  3. View Complaint
  Faculties can view the complaints from the students and they can change the
  status from not viewed to viewed
  4. Acknowledgement page
  Faculties can send their acknowledgements to each complaint through
  acknowledgement form
  5. Acknowledgement Admin
  Faculties can see acknowledgement messages from admin in this page
  6. View Profile
  Details of the Faculty can be seen in the user profile.
  7. Logout
  Students can logout from their current account.

ADMIN MODULE
  1. Home page
  Home page consists of header,footer and services page. Header complaint
  register,login and home
  2. Login page
  Admin can login to their account by entering email and password.
  3. View Student
  Admin can view the complaints from the students and registered students.
  Admin can also delete the register students
  4. Add faculty
  Admin can add Trainer,HR,Operation Head to faculty table using add faculty
  form
  5. View faculty
  Admin can view the added faculties from the view faculty table.
  6. Acknowledgement
  Admin can send the acknowledgement to the faculties who have not viewed
  the student complaint using the acknowledgement form.
  7. View Profile
  Details of the Faculty can be seen in the user profile.
  8. Logout
  Students can logout from their current account.



