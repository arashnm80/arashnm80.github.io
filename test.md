---
layout: default
title: Your Page Title
---

<!-- Include Bootstrap CSS -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

<style>
    /* Custom styles for buttons in the body */
    .body-buttons {
        cursor: pointer;
        margin: 5px;
        /* Additional custom styles as needed */
    }
</style>

<div class="container mt-5">
    <!-- Body buttons within a specific container -->
    <div class="body-buttons">
        <button onclick="filterItems('habit')" class="btn btn-outline-secondary">⬤ habit</button>
        <button onclick="filterItems('exercise')" class="btn btn-outline-secondary">⬤ exercise</button>
        <button onclick="filterItems('study')" class="btn btn-outline-secondary">⬤ study</button>
    </div>
</div>

<!-- Optional: Include Bootstrap JS for certain features -->
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
