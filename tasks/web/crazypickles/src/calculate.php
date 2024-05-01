<?php

require_once 'vendor/autoload.php';

$loader = new \Twig\Loader\FilesystemLoader('templates');
$twig = new \Twig\Environment($loader);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $card_number = $_POST['card_number'];

    $templateString = 'PICKLE ' . $card_number . '!';

    $template = $twig->createTemplate($templateString);

    $output = $template->render(['secret' => 'Pass@123']);

    echo '<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>CrazyPickles</title>
        <style>
            .user-name {
                font-size: 48px;
                font-family: \'Impact\', sans-serif;
                text-align: center;
                margin-bottom: 30px;
            }
        </style>
    </head>
    <body>
        <div class="user-name">Your name: ' . $output . '</div>
    </body>
    </html>';
}
?>