import jsonfile from "jsonfile";
import moment from "moment";
import simpleGit from "simple-git";
import random from "random";

const path = "./data.json";
const git = simpleGit();

const markCommit = (date, callback) => {
  const data = { date: date };

  jsonfile.writeFile(path, data, (err) => {
    if (err) return console.error("File write error:", err);

    git.add([path]).commit(date, {
      "--date": date,
      "--author": `U7ama<u7amajutt@gmail.com>`,
    }, (err) => {
      if (err) return console.error("Commit error:", err);
      console.log("Committed on:", date);
      callback();
    });
  });
};

const getRandomDateBetweenRange = (startDate, endDate) => {
  const start = moment.utc(startDate);
  const end = moment.utc(endDate);

  const randomTimestamp = random.int(start.valueOf(), end.valueOf());
  
  return moment.utc(randomTimestamp).toISOString();
};

const makeCommits = (n, startDate, endDate) => {
  if (n === 0) {
    console.log("All commits made. Pushing to remote...");
    return git.push();
  }

  const date = getRandomDateBetweenRange(startDate, endDate);

  markCommit(date, () => makeCommits(n - 1, startDate, endDate)); 
};

const startDate = "2022-01-01T00:00:00Z";
const endDate = "2022-12-31T23:59:59Z";

makeCommits(100, startDate, endDate);
//end