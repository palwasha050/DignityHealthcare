<?php
require('stripe-php-master/init.php');

$publishableKey="pk_test_51MRJb5EUKaz3yPwvnp2tW0FRTpint62SVZ2vD7uR0V2szVzeFsqVwig0BuXMc0P0CBUqHBfeC58PJy1eeEKP7deH00zmo05p2S";

$secretKey="sk_test_51MRJb5EUKaz3yPwv5rs3zUhS3FzlEuKYncwG0FPk9TNaSfgYhEE8updmNMTRFymYvYfNZVP86nxrGXPg7VaTOzxG00EkjKOUOV";

\Stripe\Stripe::setApiKey($secretKey);
?>