const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const mqtt = require('mqtt');
const path = require('path');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, '..', 'Frontend')));

app.get('/', (req, res) => {
    const filePath = path.join(__dirname, '..', 'Frontend', 'index.html');
    res.sendFile(filePath);
});

// Store MQTT client globally
let mqttClient = null;

app.post('/subscribe', (req, res) => {
    const { broker, port, topics } = req.body;

    if (mqttClient) {
        mqttClient.end(); // Close previous connection if exists
    }

    const topicList = topics.split(',').map(topic => topic.trim()); // Split topics into an array

    mqttClient = mqtt.connect(`mqtt://${broker}:${port}`);

    mqttClient.on('connect', () => {
        console.log('Connected to MQTT Broker!');

        topicList.forEach(topic => mqttClient.subscribe(topic));
    });

    mqttClient.on('message', (topic, message) => {
        const now = new Date();
        const hours = now.getHours();
        const minutes = now.getMinutes();
        const seconds = now.getSeconds();
        const mili = now.getMilliseconds();

        // Format the time as HH:mm:ss
        const formattedTime = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}:${mili.toString().padStart(3, '0')}`;
        console.log(formattedTime); // Output: HH:mm:ss

        const msg = {
            timestamp: formattedTime,
            topic: topic,
            payload: message.toString()
        };

        wss.clients.forEach(client => {
            if (client.readyState === WebSocket.OPEN) {
                client.send(JSON.stringify(msg));
            }
        });
    });

    res.redirect('/');
});

wss.on('connection', ws => {
    console.log('WebSocket connected!');
});

server.listen(3000, () => {
    console.log('Server running on port 3000');
});
