# QuantFrog
[![Frontend][Frontend-image]][Frontend-url]
[![Backend][Backend-image]][Backend-url]

> A project to allow access to quick data-driven predictions of quarterly earnings call for security trading.
---
## Authors

[Daniel Trinh][linkedin-urldt]
[Priyadarsi Mishra][linkedin-urlp]
[Arjun Ankad][linkedin-urlar]


## Purpose

This project was designed to aid with simplicity in mind. It is designed to provide access to 
earnings call predictions for a given security. Of course, **NO USER SHOULD**
**TAKE THIS RECOMMENDATION AS SOUND FINANCIAL ADVICE. THIS IS FOR EDUCATIONAL PURPOSES.**
We were inspired to create this project because we saw a need to make quantitative trading analysis more 
accessible. And throughout the development of this project, we experienced how difficult it
is to really get software deployed. We originally planned to have a complicated backend 
setup but were greatly limited by the available free APIs and easy to integrate databases. 
We ended up building the project using React for the easier Frontend development and a Python 
LSTM model for the intelligence behind the "advice". However, we ran into issues in connecting
the two. Originally, we had not structured the Python file in a way where it could be invoked 
by the frontend, so we needed to restructure it. But it did end up working. However, we 
do believe there is of course more work to do!


## Disclaimer
The Content is for informational purposes only, you should not construe any such 
information or other material as legal, tax, investment, financial, or other advice.
Nothing contained on our Site constitutes a solicitation, recommendation, endorsement,
or offer by the Authors or any third party service provider to buy or sell any securities 
or other financial instruments in this or in in any other jurisdiction in which such 
solicitation or offer would be unlawful under the securities laws of such jurisdiction.

All Content on this site is information of a general nature and does not address the circumstances of any particular individual or entity. Nothing in the Site constitutes professional and/or financial advice, nor does any information on the Site constitute a comprehensive or complete statement of the matters discussed or the law relating thereto. 
The Authors are not a fiduciary by virtue of any person’s use of or access to the Site or Content. You alone assume the sole responsibility of evaluating the merits and risks 
associated with the use of any information or other Content on the Site before making any decisions based on such information or other Content. In exchange for using the Site, you 
agree not to hold the Authors, its affiliates or any third party service provider liable for any possible claim for damages arising from any decision you make based on information or 
other Content made available to you through the Site.


## Deployment

Currently, the project is deployed on Vercel. This may change in the future. 


## Built With

* [Vercel](https://vercel.com/) - Frontend Hosting
* [Heroku ](https://devcenter.heroku.com/) - To deploy on Heroku
* [React JS](https://react.dev/) - Frontend Framework
* [Python 3](https://www.python.org/) - Backend Language
* [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Backend Framework


---

## Thank you for your support!


<!-- Markdown link & img dfn's -->

[repository-url]: https://github.com/priyadarsimishra/QuantFrog

[cloud-provider-url]: https://wbshopping.herokuapp.com

[linkedin-urldt]: https://www.linkedin.com/in/danielbtrinh
[linkedin-urlp]: https://www.linkedin.com/in/priyadarsi-mishra/
[linkedin-urlar]: https://www.linkedin.com/in/arjun-ankad-428b261b8/
