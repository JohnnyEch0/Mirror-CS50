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


-- read the police interviews and select the ones concerning our theft
SELECT name, transcript FROM interviews WHERE
    month = 7 AND day = 28 AND year = 2023;

-- switch to .output stdout


-- Eugene: I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

SELECT account_number, transaction_type, amount FROM atm_transactions WHERE
    month = 7 AND day = 28 AND year = 2023 AND atm_location = 'Leggett Street';

-- Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--      In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--      The thief then asked the person on the other end of the phone to purchase the flight ticket.
