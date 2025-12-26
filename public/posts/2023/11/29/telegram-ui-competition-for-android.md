---
layout: post
title:  "Telegram UI Competition for Android"
categories: posts
excerpt_separator: <!--more-->
---
Telegram is hosting a competition for Android developers to implement a new animation for deleting messages. \
![Telegram UI Competition for Android](https://github.com/arashnm80/arashnm80.github.io/assets/20334281/aad45df0-50bc-4bb7-b551-f14e26ae8f40)


<!--more-->

**Prize fund**: Up to $30,000 \
**Deadline**: 23:59 on December 7th (Dubai time) \
**Who can participate**: Everyone \
**Results**: December 15th, 2023


### The Task: 
Implement a new animation flow for deleting messages into [Telegram for Android](https://github.com/DrKLO/Telegram) similar to the [provided demo](https://t.me/contest/351) (the demo is a recording of a beta feature on Telegram for iOS). Your solution should support all entity types for both incoming and outgoing messages across all types of chats and channels. 

The most preferable outcome is likely to be achieved by taking the component [SpoilerEffect2.java](https://github.com/DrKLO/Telegram/blob/220f6b4d73793c57ba6f9023b8d38d171f342a7e/TMessagesProj/src/main/java/org/telegram/ui/Components/spoilers/SpoilerEffect2.java) as a reference. However, you may opt for your own approach as long as **no third-party UI frameworks** are used.

### Evaluation Criteria:
The primary criteria for determining a winner will be the app's **stability and performance** while replicating the provided demo **as closely as possible** (the animation in general, also the particle flow and dispersion). 

Your app **must be free** of **significant flaws** *(including crashes, visual glitches, noticeable element blinking, layout errors, and more).*

### Devices:
During the evaluation stage, submissions will be tested on a broad range of devices and Android versions (Android 7-13) not limited to the mentioned below: \
• Samsung Galaxy (A12, A32, A51, S22 Ultra) \
• Xiaomi Redmi (9, 9A, Note 8 Pro, Note 11) \
• POCO (X3 Pro) \
• Oppo (A54).

> [Telegram for Android](https://github.com/DrKLO/Telegram) utilizes performance classification with `SharedConfig.getDevicePerformanceClass()` – each device is defined as HIGH, AVERAGE or LOW. In order for your app to qualify for a reward, your solution must work flawlessly on HIGH and AVERAGE devices. Introducing a proper implementation for LOW devices will be considered a bonus.

### Submissions:
Contestants will be able to submit their entries to [@ContestBot](https://t.me/ContestBot) later. We will further clarify the submission instructions closer to the deadline.

**P.S. Winners may be offered a chance to explore further cooperation opportunities with Telegram.**

### Related links
- post in official telegram contests channel: [https://t.me/contest/350](https://t.me/contest/350)
