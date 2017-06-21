This is used in the process of creating a json file used with [`react-intl`](https://github.com/yahoo/react-intl).

Say you receive a PO file from your translation service. "I can't use this" you say. I need it in JSON, in this format:

```
{
    "id": "test",
    ...
}
```

So you do `po2csv myFile.po translated.csv`.

Now you have a CSV. This script takes it from there, and converts that CSV into a JSON file that you can drop in to your `react-intl` React app.

To use it with default settings, download the file to your Mac and run `python main.py`.

Current issues:

- There may be some problems with quotes
- It adds a comma to the last row of your JSON, which is invalid. I manually nick it for now.

Feel free to help me out by submitting a PR to fix any of the issues above. I may get to it sooner or later.
