// Dầu tiên mấy ông tạo project nodejs 

// sau đó install: npm install mqtt --save

// done

// Login Adafruit: 
    /*
    username: dangnguyen
    pass: Dang1012
    Dashboard: https://io.adafruit.com/dangnguyen/dashboards 
    feed : https://io.adafruit.com/dangnguyen/feeds
    */

    feed = [
        "dangnguyen/feeds/button1", 
        "dangnguyen/feeds/button2",
        "dangnguyen/feeds/FanValue",
        "dangnguyen/feeds/LightValue",
        "dangnguyen/feeds/sensor1",
        "dangnguyen/feeds/sensor2"
    ]
    
    const mqtt = require('mqtt')
    client = mqtt.connect({
        host: "io.adafruit.com",
        port: 1883,
        protocol: (parseInt(1883) === 8883 ? 'mqtts' : 'mqtt'),
        username: "dangnguyen",
        password: "aio_sOMP53zN1nXzWToywwZ0Y5ay98ar",
        connectTimeout: 60 * 1000,
        keepalive: 3600
      });
    
    // đẩy dữ liệu lên thử server: 
    
    
    
    // publish(topic, message, [options], [callback])
    client.publish("dangnguyen/feeds/sensor1/json", "24");

    // xong mấy ông lên kiểm tra đashboard thử log nó có ghi đúng ko
    // Cái publish này mấy ông dùng để gán vào máy cái event khi nhấn nút, 
    // ví dụ bấm vào công tắt quạt trên app khi đang ở trạng thái OFF thì nó sẽ ON và gửi lên server.
    // done
    client.end();
    // tài liệu kham khảo: https://www.npmjs.com/package/mqtt#publish