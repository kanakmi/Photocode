const { Client, PrivateKey, AccountCreateTransaction, AccountBalanceQuery, Hbar, ConsensusTopicCreateTransaction, ConsensusMessageSubmitTransaction} = require("@hashgraph/sdk");
require("dotenv").config();

async function main() {

    const myClient = Client.forTestnet();
    myClient.setOperator(process.env.ACCOUNT_ID, process.env.PRIVATE_KEY);

    const transactionId = await new ConsensusTopicCreateTransaction().execute(myClient);
    const transactionReceipt = await transactionId.getReceipt(myClient);
    const topicId = transactionReceipt.getConsensusTopicId();

    console.log("Topic ID is: ", topicId);

    for(var i=0; i<10; i++){
        var hcsMessage = await new ConsensusMessageSubmitTransaction().setTopicId(topicId).setMessage(`Hello, HCS! from Message $ {i}`).execute(myClient);
        var hcsMessageReceipt = await hcsMessage.getReceipt(myClient);

        console.log(`Sent message ${i}: ${hcsMessageReceipt.toString()}`);
    }
}
main();
