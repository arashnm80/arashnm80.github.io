layout: post
title:  "Serverless Telegram Bot With Database Channel"
categories: posts
excerpt_separator: <!--more-->
---
In this tutorial I teach you how to create a telegram bot without server that answers clients from stored messages in a database channel. We use cloudflare workers for our goal and you don't need to know programming.
<!--more-->
## Steps:
- create an account in [cloudflare.com](https://www.cloudflare.com/). Don't worry it's free.
- Go to `your dashboard in cloudflare` > `Workers & Pages` > `Create application` > `Create Worker` > choose any name and click on `Deploy`
- Click on `Edit code`
- Delete the default codes and paste my codes from [here](https://github.com/arashnm80/worker-telegram-bot-with-database-channel/blob/main/worker.js) instead
- Create a new bot in telegram via [@BotFather](https://t.me/BotFather). Get the `HTTP API` from BotFather and paste it in `TOKEN` value of worker's code.
- Create a database channel for yourself and make your bot an admin of it. Put the channel's username with beginning `@` in the `databaseChannel` value of the worker's code.
- Write some random text made up from letters and numbers in the `SECRET` value of worker's code. this secret's job is to make your bot safe.
- Finally edit the `commands` in worker's code like the given template. commands can be with or without slashes and in any language. In front of each command write a number which is the message Id of the response in your database channel. (If you don't know Id of a message you can simply copy the link of message and the check it, the last number after slash is the message Id)
- If it's the first time that you are running the bot add `registerWebhook` to the end of worker address and click on `send`. after that point, every time that you decide to edit commands a simple `Save and Deploy` will be sufficient.