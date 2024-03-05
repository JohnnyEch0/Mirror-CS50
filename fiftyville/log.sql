-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check the Crime Scene reports for matching Reports
SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street' AND month = 7 AND day = 28;

-- all 3 witnesses mention the bakery
-- Time: 10:15am
-- also there was a littering

-- read the bakeries sec logs at the given hour, sort by time
SELECT activity, license_plate, hour, minute FROM bakery_security_logs WHERE
    month = 7 AND day = 28 AND year = 2023 AND hour = 10 ORDER BY hour;

-- rerun with .output results.txt bc i cant copy from the terminal


