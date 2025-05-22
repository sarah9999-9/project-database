
INSERT INTO Laboratorian VALUES
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


INSERT INTO Patient VALUES
(1001, 'Mohamed Salah', '0111111111', 'Cairo', '1985-07-15', 'Engineer'),
(1002, 'Fatma Ahmed', '0122222222', 'Alexandria', '1990-03-20', 'Teacher'),
(1003, 'Hany Mahmoud', '0103333333', 'Giza', '1975-11-05', 'Doctor'),
(1004, 'Laila Hassan', '0114444444', 'Cairo', '1988-06-30', 'Nurse'),
(1005, 'Ali Mohamed', '0125555555', 'Tanta', '1992-01-10', 'Student'),
(1006, 'Sara Khaled', '0106666666', 'Mansoura', '1980-12-25', 'Lawyer'),
(1007, 'Ahmed Youssef', '0117777777', 'Cairo', '1987-09-15', 'Accountant'),
(1008, 'Nora Sami', '0128888888', 'Alexandria', '1995-05-22', 'Designer'),
(1009, 'Tarek Adel', '0109999999', 'Giza', '1978-08-18', 'Architect'),
(1010, 'Dina Samir', '0110000000', 'Cairo', '1993-04-02', 'Pharmacist');


INSERT INTO Component VALUES
(1, 'Blood Sample Tube', 50, 10),
(2, 'Glucose Reagent', 30, 15),
(3, 'Hemoglobin Reagent', 40, 20),
(4, 'Microscope Slides', 60, 25),
(5, 'Urine Sample Cup', 45, 15),
(6, 'Chemical Reagent A', 20, 10),
(7, 'Chemical Reagent B', 15, 10),
(8, 'Test Tubes', 35, 10),
(9, 'Alcohol Swabs', 80, 30),
(10, 'Gloves', 100, 50);


INSERT INTO Medical_Test VALUES
(101, 'CBC', 150.00),
(102, 'Blood Sugar', 120.00),
(103, 'Urinalysis', 130.00),
(104, 'Liver Function Test', 200.00),
(105, 'Kidney Function Test', 190.00),
(106, 'Lipid Profile', 180.00),
(107, 'Thyroid Test', 170.00),
(108, 'Vitamin D Test', 160.00),
(109, 'COVID-19 PCR', 300.00),
(110, 'Electrolyte Panel', 140.00);


INSERT INTO Test_Component VALUES
(101, 1),
(101, 3),
(102, 2),
(103, 5),
(104, 6),
(105, 7),
(106, 8),
(107, 9),
(108, 10),
(109, 4),
(110, 3);


INSERT INTO Test_Result VALUES
(1, 101, '2024-04-01', 1001, 1, 'Normal CBC results'),
(2, 102, '2024-04-03', 1002, 2, 'High blood sugar level'),
(3, 103, '2024-03-30', 1003, '3', 'Normal urine analysis'),
(4, 104, '2024-04-05', 1004, 4, 'Elevated liver enzymes'),
(5, 105, '2024-04-07', 1005, 5, 'Normal kidney function'),
(6, 106, '2024-04-09', 1006, 6, 'High cholesterol'),
(7, 107, '2024-04-11', 1007, 7, 'Normal thyroid levels'),
(8, 108, '2024-04-13', 1008, 8, 'Vitamin D deficiency'),
(9, 109, '2024-04-15', 1009, 9, 'Negative COVID-19 PCR'),
(10, 110, '2024-04-17', 1010, 10, 'Normal electrolyte levels');
