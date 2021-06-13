
const MongoClient = require('mongodb').MongoClient;

const uri = "mongodb+srv://IOTProject:g7fGHthZqV2cz8E@cluster0.wzs74.mongodb.net/ProjectADM?retryWrites=true&w=majority";


const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

client.connect(err => {
  const collection = client.db("ProjectADM").collection("Electronics");
  // perform actions on the collection object
  console.log(collection.find({}).count())
 

  client.close();
});
