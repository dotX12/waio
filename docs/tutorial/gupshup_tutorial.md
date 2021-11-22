# How to work with gupshup.io

## Register

To get started, you will need to register on the website gupshup.io<br>
![](https://raw.githubusercontent.com/dotX12/waio/master/docs/assets/images/gupshup_register.png "Register")

## Create an app
Now let's create our first app. Follow the link https://www.gupshup.io/developer/whatsapp-api and click "Try sandbox for free"<br>
![](https://raw.githubusercontent.com/dotX12/waio/master/docs/assets/images/gupshup_trysandbox.png "Try sandbox")

Give your app a name<br>
![](https://raw.githubusercontent.com/dotX12/waio/master/docs/assets/images/gupshup_appname.png "Give an app name")

Set your system language preference in the App<br>
![](https://raw.githubusercontent.com/dotX12/waio/master/docs/assets/images/gupshup_language.png "Language")

Now you can see App Control Panel<br>
![](https://raw.githubusercontent.com/dotX12/waio/master/docs/assets/images/gupshup_panel.png "Control panel")

## Webhooks
You can carry out the work using webhooks. To use webhooks with gupshup, let's install ngrok. <br>
1. Download ngrok https://ngrok.com/download <br>
2. Connect your ngrok account `./ngrok authtoken <your_auth_token>` (in terminal or CMD) <br>
3. Start a HTTP tunnel on port 8017 `./ngrok http 8017` (in terminal or CMD) <br>
4. Now you have link like _https://1155-77-82-30-65.ngrok.io_ <br>
5. Create and run a bot until you see (You can use <a href="https://github.com/dotX12/waio/tree/master/examples/first_bot">This example</a>) <br>
```
======== Running on http://0.0.0.0:8017 ========
(Press CTRL+C to quit)
```
6. Paste the link into your app settings<br>
![](https://raw.githubusercontent.com/dotX12/waio/master/docs/assets/images/gupshup_webhook.png "Set webhook")

_Don't forget to add /api/v1/gupshup/hook to the link and enable the use of webhooks, as shown in the picture_

## Use bot
To use the bot, write in WhatsApp to bot's number "proxy <your_app_name>" <br>
Now you are communicating with your bot


