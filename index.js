const express = require('express');
const app = express();

// 1. Middleware to allow the API to read JSON data sent in the request body
app.use(express.json());

// 2. The Endpoint Definition
// We use app.post because your requirement specifies a POST request
app.post('/api/voice-detection', (req, res) => {
    
    // 3. API Key Authentication (The "Bouncer")
    const apiKey = req.headers['x-api-key'];
    const SECRET_KEY = "process.env.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"; // In production, use process.env.X_API_KEY

    if (!apiKey || apiKey !== SECRET_KEY) {
        return res.status(401).json({
            error: "Unauthorized",
            message: "Invalid or missing API Key"
        });
    }

    // 4. Logic for Voice Detection (Placeholder)
    // Here you would process the voice data sent in req.body
    console.log("Request received with data:", req.body);

    // 5. Success Response
    res.status(200).json({
        success: true,
        message: "Voice detection processed successfully",
        detected_text: "Hello world" 
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
