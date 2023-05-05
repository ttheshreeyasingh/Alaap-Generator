const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');

const app = express();

app.use(bodyParser.json());

app.post('/run-script', (req, res) => {
  exec('python driver.py && python swara_to_music.py', (err, stdout, stderr) => {
    if (err) {
      console.log(err);
      return res.status(500).send('Script execution failed!');
    }
    console.log(stdout);
    res.send('Script executed successfully!');
  });
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
