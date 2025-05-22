# Medical Laboratory System Database Project
  
Sarah Yaser, Mohamed Reda, Mohamed Khalf, Asmaa Ragb  
**Supervisor:** Dr. Mohamed ELSayeh

---

## 1. Project Summary

This project is about designing and building a database system for a medical laboratory. The system helps manage laboratorians, patients, medical tests, test components, and test results. It supports the daily work of the lab by tracking test materials, saving test results accurately, and making it easy to find information about patients and their tests.

We also made a desktop application using Python and Tkinter that lets users manage the lab data easily without writing SQL commands.

---

## 2. Conceptual Design and ER Diagram

The main parts of the system are:

- **Laboratorian:** The person who does the tests.  
- **Patient:** The person who takes the tests.  
- **Medical Test:** The tests available in the lab.  
- **Component:** Materials used for tests.  
- **Test Component:** Connects tests and their components (many-to-many).  
- **Test Result:** The results of tests done for patients by laboratorians.

The ER diagram shows:  
- One laboratorian can do many test results.  
- One patient can have many test results.  
- Tests and components have a many-to-many relationship through Test Component.  
- Every test result must have a patient and a laboratorian.



---

## 3. Database Tables and SQL

We created tables for all the parts above.  
Each table has a primary key to identify records and foreign keys to link related tables.

The tables are:  
- Laboratorian  
- Patient  
- Component  
- Medical_Test  
- Test_Component (links tests and components)  
- Test_Result

SQL scripts to create these tables and add sample data are in the file `CREATE_TABLES.sql`.

---

## 4. Sample Data

We added at least 10 records to each table to make the database useful for testing and examples.
(1, 'Ahmed Ali', '0123456789', 'Cairo'),  

(2, 'Mona Hassan', '0112233445', 'Alexandria'), 

 (3, 'Omar Saeed', '0156789456', 'Giza'), 

 (4, 'Sara Khaled', '0109988776', 'Cairo'), 

 (5, 'Ali Mahmoud', '0123344556', 'Tanta'),  

(6, 'Hana Youssef', '0115566778', 'Mansoura'),  

(7, 'Khaled Farag', '0101234567', 'Cairo'), 

 (8, 'Nadia Ibrahim', '0129876543', 'Alexandria'),  

(9, 'Tamer Adel', '0111112222', 'Cairo'), 

 (10, 'Dina Samir', '0122223333', 'Giza'); 

---

## 5. Example Queries

Some useful SQL queries are:

- Find patients who took the CBC test in the last year.  
- Find components that have less quantity than the minimum needed.  
- Find how much money a patient paid for tests in the last 3 years.

---

## 6. Application Overview

We built a desktop app in Python with Tkinter. It lets users:  
- Add, update, delete, and see laboratorians, patients, components, tests, and results.  
- Use a simple window with tabs for each part.  
- The app creates the database and loads sample data automatically when you run it for the first time.

---

## 7. How to Run the Project

1. Make sure Python 3 is installed on your computer.  
2. Open your terminal or command prompt.  
3. Go to the project folder.  
4. Run this command:  
