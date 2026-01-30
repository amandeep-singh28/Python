select first_name, last_name
from patients
where allergies is null;

select allergies from patients;

select first_name
from patients
where first_name like "C%";

select first_name, last_name
from patients
where weight >= 100 and weight <= 120;

select first_name, last_name
from patients
where weight between 100 and 120;

update patients
SET allergies = "NKA"
where allergies is null;

select concat(first_name, " ", last_name) as full_name
from patients;

select first_name, last_name, province_name
from patients
JOIN province_names
ON patients.province_id = province_names.province_id;


select count(patient_id) as total_patients
from patients
where birth_date like "2010%";

select birth_date from patients;


select first_name, last_name, height
from patients WHERE height = 
(select MAX(HEIGHT) FROM patients);


select * from patients where patient_id IN
(1, 45, 534, 879, 1000);

select count(patient_id) as total_admissions from admissions;

select * from admissions
where
admission_date = discharge_date;

select patient_id, count(patient_id) as total_admissions
from admissions
where patient_id = 579;

select distinct(city) as unique_cities
from patients
where province_id = 'NS';

select first_name, last_name, birth_date
from patients
where height > 160 and weight > 70;

select first_name, last_name, allergies
from patients where
allergies is not null and city = "Hamilton";


-- Medium Questions

select DISTINCT(year(birth_date)) as birth_year
from patients
ORDER BY birth_year ASC

select first_name
from patients
group by first_name
having count(first_name) = 1;

select patient_id, first_name
from patients
where first_name like "s%s" and len(first_name) >= 6;

select patient_id, first_name, last_name
from patients where patient_id IN
(select patient_id
from admissions
where diagnosis = "Dementia");

select first_name
from patients
order by len(first_name) ASC, first_name ASC;

select count(patient_id) as male_count, 4530 - count(patient_id) as female_count
from patients
where gender = "M";

select first_name, last_name, allergies
from patients
where allergies = 'Penicillin' or allergies = 'Morphine'
order by allergies ASC,first_name asc, last_name ASC;

SELECT patient_id, diagnosis
FROM admissions
GROUP BY patient_id, diagnosis
HAVING COUNT(*) > 1;


select city, count(patient_id) as num_patients
from patients
GROUP BY CITY
order by num_patients DESC, city ASC;

SELECT first_name, last_name, 'Patient' AS role
FROM patients

UNION ALL

SELECT first_name, last_name, 'Doctor' AS role
FROM doctors;


select allergies, count(allergies) as total_diagnosis
from patients
where allergies is not null
group by allergies
order by total_diagnosis DESC;

select first_name, last_name, birth_date
from patients
where year(birth_date) >= 1970 and year(birth_date) < 1980
order by birth_date ASC;

select concat(upper(last_name), ",", lower(first_name))
from patients
order by first_name DESC;

select province_id, sum(height)
from patients
group by province_id
having sum(height) >= 7000;

select (max(weight) - min(weight)) as weight_delta
from patients
where last_name = "Maroni";

select day(admission_date) as day_number, count(patient_id) as number_of_admissions
from admissions
group by day_number
order by number_of_admissions DESC;

select *
from admissions
where patient_id = 542
order by admission_date DESC
LIMIT 1;

select patient_id, attending_doctor_id, diagnosis
from admissions
where
((patient_id % 2 <> 0) AND (attending_doctor_id IN (1, 5, 19)))
OR
((attending_doctor_id like "%2%") AND (len(patient_id) = 3));

select first_name, last_name, count(patient_id) as admissions_total
from doctors
INNER join
admissions ON
admissions.attending_doctor_id = doctors.doctor_id
group by first_name, last_name;

select doctor_id, concat(first_name, " ", last_name) as full_name, min(admission_date) as first_admission_date, max(admission_date) as last_admission_date
from doctors
INNER JOIN
admissions ON
doctors.doctor_id = admissions.attending_doctor_id
group by doctor_id;

select province_name, count(patient_id) as patient_count
from province_names
INNER JOIN
patients ON
province_names.province_id = patients.province_id
GROUP BY province_name
order by patient_count DESC;
