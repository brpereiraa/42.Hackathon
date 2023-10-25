<?php

    $serverName = "localhost";
    $dbUsername = "user";
    $dbPassword = "H@ckathon#42";
    $dbName = "mydb";

    $conn = mysqli_connect($serverName, $dbUsername, $dbPassword, $dbName);

    if (!$conn){
        die("Connection failed: " . mysqli_connect_error());
    }

    session_start();
?>