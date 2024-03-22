const querystring = require("querystring");
const axios = require("axios");

// TOKEN from https://oauth.vk.com/authorize?client_id=7432908&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=groups&response_type=token&v=5.131&state=123456
// or GROUP_TOKEN
const TOKEN = "";

// ids of users
const str = "";

const timer = (ms) => new Promise((res) => setTimeout(res, ms));

async function load() {
  // We need to wrap the loop into an async function for this to work
  const users = str.split(",");
  console.log(users.length);

  for (const user of users) {
    console.log(user);

    const data = {
      group_id: 224129790,
      user_id: user,
      access_token: TOKEN,
      v: "5.199",
    };

    await axios.post(
      "https://api.vk.com/method/groups.removeUser",
      querystring.stringify(data),
      {
        "Content-Type": "multipart/form-data",
      }
    );

    await timer(1000);
  }
}

load();
