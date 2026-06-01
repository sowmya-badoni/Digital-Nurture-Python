# ANSI SQL Using MySQL – 25 SQL Practice Questions

This repository contains solutions for 25 ANSI SQL practice questions based on an Event Management Database schema consisting of:

- Users
- Events
- Sessions
- Registrations
- Feedback
- Resources

The exercises cover SQL concepts such as:

- Joins
- Aggregation
- GROUP BY
- HAVING
- Subqueries
- CTEs
- Date Functions
- Window Analysis
- Data Validation
- Reporting Queries

---

# Sample Dataset

## Users Table

<img src="Task Solution Images/users.png" width="500">

## Events Table

<img src="Task Solution Images/events.png" width="500">

## Sessions Table

<img src="Task Solution Images/sessions.png" width="500">

## Registrations Table

<img src="Task Solution Images/registrations.png" width="500">

## Feedback Table

<img src="Task Solution Images/feedback.png" width="500">

## Resources Table

<img src="Task Solution Images/resources.png" width="500">

---

# SQL Exercises

## 1. User Upcoming Events

**Problem Statement**

Show a list of all upcoming events a user is registered for in their city, sorted by date.

### Output

<img src="Task Solution Images/task1.png" width="500">

---

## 2. Top Rated Events

**Problem Statement**

Identify events with the highest average rating, considering only those that have received at least 10 feedback submissions.

### Output

<img src="Task Solution Images/task2.png" width="500">

---

## 3. Inactive Users

**Problem Statement**

Retrieve users who have not registered for any events in the last 90 days.

### Output

<img src="Task Solution Images/task3.png" width="500">

---

## 4. Peak Session Hours

**Problem Statement**

Count how many sessions are scheduled between 10 AM and 12 PM for each event.

### Output

<img src="Task Solution Images/task4.png" width="500">

---

## 5. Most Active Cities

**Problem Statement**

List the top 5 cities with the highest number of distinct user registrations.

### Output

<img src="Task Solution Images/task5.png" width="500">

---

## 6. Event Resource Summary

**Problem Statement**

Generate a report showing the number of resources (PDFs, Images, Links) uploaded for each event.

### Output

<img src="Task Solution Images/task6.png" width="500">

---

## 7. Low Feedback Alerts

**Problem Statement**

List all users who gave feedback with a rating less than 3, along with their comments and associated event names.

### Output

<img src="Task Solution Images/task7.png" width="500">

---

## 8. Sessions per Upcoming Event

**Problem Statement**

Display all upcoming events with the count of sessions scheduled for them.

### Output

<img src="Task Solution Images/task8.png" width="500">

---

## 9. Organizer Event Summary

**Problem Statement**

For each event organizer, show the number of events created and their current status.

### Output

<img src="Task Solution Images/task9.png" width="500">

---

## 10. Feedback Gap

**Problem Statement**

Identify events that had registrations but received no feedback at all.

### Output

<img src="Task Solution Images/task10.png" width="500">

---

## 11. Daily New User Count

**Problem Statement**

Find the number of users who registered each day in the last 7 days.

### Output

<img src="Task Solution Images/task11.png" width="500">

---

## 12. Event with Maximum Sessions

**Problem Statement**

List the event(s) with the highest number of sessions.

### Output

<img src="Task Solution Images/task12.png" width="500">

---

## 13. Average Rating per City

**Problem Statement**

Calculate the average feedback rating of events conducted in each city.

### Output

<img src="Task Solution Images/task13.png" width="500">

---

## 14. Most Registered Events

**Problem Statement**

List the top 3 events based on the total number of user registrations.

### Output

<img src="Task Solution Images/task14.png" width="500">

---

## 15. Event Session Time Conflict

**Problem Statement**

Identify overlapping sessions within the same event.

### Output

<img src="Task Solution Images/task15.png" width="500">

---

## 16. Unregistered Active Users

**Problem Statement**

Find users who created an account in the last 30 days but haven’t registered for any events.

### Output

<img src="Task Solution Images/task16.png" width="500">

---

## 17. Multi-Session Speakers

**Problem Statement**

Identify speakers who are handling more than one session across all events.

### Output

<img src="Task Solution Images/task17.png" width="500">

---

## 18. Resource Availability Check

**Problem Statement**

List all events that do not have any resources uploaded.

### Output

<img src="Task Solution Images/task18.png" width="500">

---

## 19. Completed Events with Feedback Summary

**Problem Statement**

For completed events, show total registrations and average feedback rating.

### Output

<img src="Task Solution Images/task19.png" width="500">

---

## 20. User Engagement Index

**Problem Statement**

For each user, calculate how many events they attended and how many feedbacks they submitted.

### Output

<img src="Task Solution Images/task20.png" width="500">

---

## 21. Top Feedback Providers

**Problem Statement**

List the top 5 users who have submitted the most feedback entries.

### Output

<img src="Task Solution Images/task21.png" width="500">

---

## 22. Duplicate Registrations Check

**Problem Statement**

Detect if a user has been registered more than once for the same event.

### Output

<img src="Task Solution Images/task22.png" width="500">

---

## 23. Registration Trends

**Problem Statement**

Show a month-wise registration count trend over the past 12 months.

### Output

<img src="Task Solution Images/task23.png" width="500">

---

## 24. Average Session Duration per Event

**Problem Statement**

Compute the average duration (in minutes) of sessions in each event.

### Output

<img src="Task Solution Images/task24.png" width="500">

---

## 25. Events Without Sessions

**Problem Statement**

List all events that currently have no sessions scheduled under them.

### Output

<img src="Task Solution Images/task25.png" width="500">

---

# Technologies Used

- SQL
- ANSI SQL
- SQLite
- MySQL
- GitHub

---

# Author

**SOWMYA BADONI**

B.TECH. Artificial Intelligence and Machine Learning 
Saveetha Engineering College
