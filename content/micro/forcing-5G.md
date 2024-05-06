+++
title = "Forcing my phone to only use 5G"
date = 2024-02-19
# updated = 2024-05-06
draft = false

[taxonomies]
tags = ["networking", "internet", "phones"]

[extra]
giscus = true
+++

**Situation**: I am on a data plan that offers "unlimited data" if I am on a 5G connection, otherwise I have a limited amount of data on 4G and lower bands of the network. It has become annoying for me that my phone just spontaneously switches to 4G even if I am well within a 5G network (and, yes, I have turned off the option for "Smart 5G" that's there to save power). It also becomes a bigger headache when I run out of non-5G data since I lose access to the "unlimited data" even though I am connected on a 5G band.

**Action**: Thus, I have looked for ways to force my phone to only be in 5G mode. One of the posts I stumbled upon suggests installing an app on the Google Play Store called [Netmonitor](https://play.google.com/store/apps/details?id=com.parizene.netmonitor)[^1] in order to set the setting of my `Preferred Network Type` to `NR only`. This may be a bad idea doing something that I do not fully understand but so far it does work for quite some time now that I have tested it. The setting sometimes just reverts back when my phone kills the Netmonitor app in order to save power and prolong battery life. I resolved that immediately with some fiddling with the battery settings and locking the app in the recent apps screen.

However, in the end, one big problem that I cannot resolve is the lack of proper standalone 5G towers in the area I'm currently residing at. Looking at the app, there's seems to be only `LTE Advanced + 5G (NSA)` cell towers at most (and the signal sometimes gets lost and only 4G is available). Making it hard to actually get my money's worth out of the "unlimited" 5G data + extra 12GB data (non-5G) data plan.

It seems like this mobile data plan was too good to be true and the catch is in the technical details that a layperson might not see. Given the sparse 5G infrastructure and (possibly) deprioritization of your requests in the network because of having "unlimited" data, it's probably to better to go with the conventional optical fiber plans for your internet connection unless you only have mobile data available to you.

<!-- Footnotes -->
[^1]: There's also the option to dial `*#*#4636#*#*` in your Dialer app to open a hidden menu and change the setting there. However, I cannot get it to launch the hidden menu for me (probably blocked by phone manufacturer).
