# How to work with gupshup.io

## Register

To get started, you will need to register on the website gupshup.io<br>
<img src="https://i.ibb.co/zb84s4N/gupshup-register.png" align="bottom"><br>

## Create an app
Now let's create our first app. Follow the link https://www.gupshup.io/developer/whatsapp-api and click "Try sandbox for free"<br>
<img src="https://i.ibb.co/202TQpF/gupshup-trysandbox.png" align="bottom"><br>

Give your app a name<br>
<img src="https://i.ibb.co/1nQT39s/gupshup-appname.png" align="bottom"><br>

Set your system language preference in the App<br>
<img src="https://i.ibb.co/hX1QLFm/gupshup-language.png" align="bottom"><br>

Now you can see App Control Panel<br>
<img src="https://i.ibb.co/wyfswNv/gupshup-panel.png" align="bottom"><br>


## Webhooks
You can carry out the work using webhooks. To use webhooks with gupshup, let's install ngrok. 
1. Download ngrok https://ngrok.com/download
2. Connect your ngrok account `./ngrok authtoken <your_auth_token>` (in terminal or CMD)
3. Start a HTTP tunnel on port 8017 `./ngrok http 8017` (in terminal or CMD)
4. Now you have link like _https://1155-77-82-30-65.ngrok.io_
5. Create and run a bot until you see (You can use <a href="https://github.com/dotX12/waio/tree/master/examples/first_bot">This example</a>) <br>
```
======== Running on http://0.0.0.0:8017 ========
(Press CTRL+C to quit)
```
6. Paste the link into your app settings<br>
<img src="https://i.ibb.co/ZgtF22L/gupshup-webhook.png" align="bottom"><br>

_Don't forget to add /api/v1/gupshup/hook to the link and enable the use of webhooks, as shown in the picture_

## Use bot
To use the bot, write in WhatsApp to bot's number "proxy <your_app_name>" <br>
Now you are communicating with your bot


