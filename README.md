## Move-O-Matic

Move-O-Matic was an ADHD side quest whilst moving house to try and automate label printing using the awesome [blabel](https://github.com/Edinburgh-Genome-Foundry/blabel) to generate labels from HTML/CSS and Ghostscript to send the labels to my label printer.

![Move-O-Matic](img/move-o-matic.gif)

I was using this for 50mmx30mm labels on an ancient Thermal Transfer Printer. Any size would work, the app uses blabel to create labels as PDF, then sends the PDF to a nominated printer using a cli call to Ghostscript. Be afraid, this is *very* crudely written, everything about it is shocking, but I'm currently midst move and it's working just dandy. 

Hopefully this helps someone as well. PRs very welcome. Licence = MIT