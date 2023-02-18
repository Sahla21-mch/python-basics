<?php
$server="localhost";
$username="root";
$password="";
$db="login form";
$conn = mysqli_connect ($server, $username, $password, $db);
if(isset($_POST['submit'])){
    if(!empty($_POST['name']) && !empty($_POST['email']) && !empty($_POST['address']) && !empty($_POST['password'])){
            $name=$_POST['name'];
            $email = $_POST['email'];
            $password = $_POST['password'];
            $address = $_POST['address'];
            $query = "INSERT INTO Information (name, email, password, address) values('$name', '$email', '$password', '$address')";        
            $run = mysqli_query($conn, $query) or die($mysqli_error());
            if($run){
                echo " form submitted successfully";
            } 
            else{
                echo "form not submitted";
            }
        }
    else{
     
        echo "all fields required";
    }
    
}
?>


