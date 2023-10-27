# stori_challenge

# How to process csv

- First run all docker containers using:

      make run

- Then process csv file with this command:
- (Note: csv-file and email-address are optional)

      make process-csv csv-file=some-file-address.csv email-address=some.email.address@mail.com

- Or just enter this if you want the default values:

      make process-csv

- To check the email sent enter localhost:8025 in your browser


- Finally, stop all docker containers:

      make stop