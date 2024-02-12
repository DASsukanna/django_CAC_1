/* scripts.js */

document.addEventListener("DOMContentLoaded", function () {
    // Initial dummy data
    let totalMembersData = 35;
    let newMembersGrowthData = {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [{
            label: 'New Members Growth',
            data: [10, 15, 20, 25, 30, 35],
            fill: false,
            borderColor: 'rgba(75, 192, 192, 1)',
            tension: 0.4
        }]
    };

    let ageDistributionData = {
        labels: ["0-18", "19-30", "31-50", "50+"],
        datasets: [{
            label: 'Age Distribution',
            data: [15, 30, 50, 55],
            backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    };

    let genderDistributionData = {
        labels: ["Male", "Female", "Other"],
        datasets: [{
            data: [45, 50, 5],
            backgroundColor: [
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 99, 132, 0.5)',
                'rgba(255, 206, 86, 0.5)'
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    };

    let eventAttendanceData = {
        labels: ["All-Go Rhythm", "Imperio 2024", " Gladiators 2024", "Alumni Meet", "Darpan 2024"],
        datasets: [{
            label: 'Attendance',
            data: [50, 75, 60, 90, 80],
            backgroundColor: 'rgba(255, 99, 132, 0.7)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    };

    let memberSkillsData = {
        labels: ["Varsity Game Club", "Radio Club", "SWO", "Trekking Club", "Writer's Club"],
        datasets: [{
            label: 'Clubs',
            data: [80, 60, 45, 70, 90],
            fill: true,
            backgroundColor: 'rgba(255, 206, 86, 0.7)',
            borderColor: 'rgba(255, 206, 86, 1)',
            borderWidth: 1
        }]
    };

    // Update card values and draw initial charts
    document.getElementById("totalMembers").innerText = totalMembersData;
    drawNewMembersGrowthChart(newMembersGrowthData);
    drawAgeDistributionChart(ageDistributionData);
    drawGenderDistributionChart(genderDistributionData);
    drawEventAttendanceChart(eventAttendanceData);
    drawMemberSkillsChart(memberSkillsData);
});

function addClub() {
    // Simulate adding new members after an event
    let newMembersGrowthData = {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [{
            label: 'New Members Growth',
            data: [10, 15, 20, 25, 30, 35],
            fill: false,
            borderColor: 'rgba(75, 192, 192, 1)',
            tension: 0.4
        }]
    };
    drawNewMembersGrowthChart(newMembersGrowthData);
}

function removeClub() {
    // Simulate adding new members after an event
    let newMembersGrowthData = {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [{
            label: 'New Members Growth',
            data: [10, 15, 20, 25, 30, 35],
            fill: false,
            borderColor: 'rgba(75, 192, 192, 1)',
            tension: 0.4
        }]
    };
    drawNewMembersGrowthChart(newMembersGrowthData);
}

function updateClubDetaisl() {
    // Simulate adding new members after an event
    let newMembersGrowthData = {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [{
            label: 'New Members Growth',
            data: [10, 15, 20, 25, 30, 35],
            fill: false,
            borderColor: 'rgba(75, 192, 192, 1)',
            tension: 0.4
        }]
    };
    drawNewMembersGrowthChart(newMembersGrowthData);
}

function drawNewMembersGrowthChart(data) {
    let ctx = document.getElementById("newMembersGrowthChart").getContext("2d");
    new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

function drawAgeDistributionChart(data) {
    let ctx = document.getElementById("ageDistributionChart").getContext("2d");
    new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

function drawGenderDistributionChart(data) {
    let ctx = document.getElementById("genderDistributionChart").getContext("2d");
    new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

function drawEventAttendanceChart(data) {
    let ctx = document.getElementById("eventAttendanceChart").getContext("2d");
    new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}

function drawMemberSkillsChart(data) {
    let ctx = document.getElementById("memberSkillsChart").getContext("2d");
    new Chart(ctx, {
        type: 'radar',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
}
