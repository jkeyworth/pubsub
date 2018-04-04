import paho.mqtt.client as mqtt
import time


class ConnectionManager:

    __subscriptions = {}

    def __init__(self, id, host_name, host_port):
        self.client = mqtt.Client(id)
        self.host_name = host_name
        self.host_port = host_port
        self.is_connected = False
        self.client.on_message = self.__on_message

    def __on_message(self, client, userdata, message):
        print("message received")
        self.__subscriptions[message.topic](client, userdata, message)

    def __connect(self):
        self.client.connect(self.host_name, port=self.host_port)
        self.client.loop_start()
        self.is_connected = True

    def __disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        self.is_connected = False

    def __publish_message_to_topic(self, topic, message):
        self.client.publish(topic, message)

    def publish(self, topic, message):
        if self.is_connected:
            self.__publish_message_to_topic(topic, message)
        else:
            self.__connect()
            self.__publish_message_to_topic(topic, message)
            self.__disconnect()

    def subscribe(self, topic, on_message):
        if not self.is_connected:
            self.__connect()
        self.client.subscribe(topic)
        self.__subscriptions[topic] = on_message

if __name__ == "__main__":
    def print_message(client, userdata, message):
        print("message received", str(message.payload.decode("utf-8")))

    mgr = ConnectionManager("mac_test", "test.mosquitto.org", 1883)
    mgr.subscribe("house/lounge/motion", print_message)
    mgr.publish("house/lounge/motion", "test message")
    time.sleep(5)
