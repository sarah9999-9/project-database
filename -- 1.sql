-- 1. List the names of patients who performed the CBC test in the last year
SELECT DISTINCT p.name
FROM Patient p
JOIN Test_Result tr ON p.Patient_ID = tr.Patient_ID
JOIN Medical_Test mt ON tr.Test_ID = mt.Test_ID
WHERE mt.name = 'CBC' AND tr.date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

-- 2. List the names of components where the available quantity is less than the minimum quantity
SELECT name, available_quantity, minimum_quantity
FROM Component
WHERE available_quantity < minimum_quantity;

-- 3. Calculate the total amount paid by a patient with Patient_ID = 12527 in the last 3 years
SELECT p.name, SUM(mt.price) AS total_paid
FROM Patient p
JOIN Test_Result tr ON p.Patient_ID = tr.Patient_ID
JOIN Medical_Test mt ON tr.Test_ID = mt.Test_ID
WHERE p.Patient_ID = 12527 AND tr.date >= DATE_SUB(CURDATE(), INTERVAL 3 YEAR)
GROUP BY p.Patient_ID;
