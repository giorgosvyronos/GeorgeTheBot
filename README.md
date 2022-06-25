# George The Bot

George The Bot is a Tweeter Bot built out of fun and recreation.

## Use

This is a free internet. This bot can't be used. It can only be observed.


## Project Structure
```
GeorgeTheBot/
├── venv/
│
├── src/
│   ├── lambda_function.py
│   └── tweets.csv
│
├── .env
├── buildpackage.sh
├── createlambdalayer.sh 
├── entrypoint.py
├── LICENSE
├── README.md
└── requirements.txt
```
### Files:
- `venv/`: Virtual environment with the libraries your project requires
- `src/lambda_function.py`: Python script containing the logic of your bot. You'll package this code and upload it to the AWS Lambda function.
- `src/tweets.csv`: List of predefined tweets your bot uses for posting. This also goes in the package you'll upload to the Lambda function.
- `.env`: File containing your credentials to authenticate the Twitter API. It's used for testing your bot locally.
- `buildpackage.sh`: Utility function that packages the contents of `src/` into a file called `lambda_function.zip`. You'll upload this file to the Lambda function.
- `createlambdalayer.sh`: Utility function that packages the libraries specified in requirements into a file called `layer.zip`. You'll upload this file to a Lambda Layer.
- `entrypoint.py`: Python script you'll use for testing your bot locally.
- `requirements.txt`: Standard way of specifying the libraries your project requires.
- `LICENSE` and `README.md`: License and description of the repository.

## To Do List
- [x] Instantiate code for twitter bot.
- [ ] Follow https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/ to build bot on AWS Lambda.
- [ ] Add support and integration of OpenAI model to create randomized tweets.
- [ ] Add support to choose between random tweet or posting custom tweet.
- [ ] Add control over mobile application.

## Contributing
Pull requests are welcome. Don't be afraid to drop me a message for anything. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GENERAL PUBLIC LICENSE](LICENSE.md)

### Origin

This project was created by Giorgos Vyronos, based on the guidelines of [Dylan J Castillo](https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/)