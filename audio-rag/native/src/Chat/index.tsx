import React, {Dispatch, SetStateAction, useState} from 'react';
import {StyleSheet, Text, TextInput} from 'react-native';
import {Message} from './types';
import {MessagesView} from './MessagesView';
import {queueMessage} from './utils';

export const Chat = ({
  messages,
  setMessages,
}: {
  messages: Message[];
  setMessages: Dispatch<SetStateAction<Message[]>>;
}) => {
  const [message, setMessage] = useState('');
  return (
    <>
      <Text style={styles.title}>Chat with store</Text>
      <MessagesView messages={messages} />

      <TextInput
        style={styles.input}
        value={message}
        onChangeText={text => setMessage(text)}
        placeholder="Send a message..."
        onSubmitEditing={() => {
          setMessage('');
          setMessages(mgs => {
            return mgs.concat([
              {
                author: 'User',
                content: message,
              },
            ]);
          });
          queueMessage(message, setMessages);
        }}
      />
    </>
  );
};

const styles = StyleSheet.create({
  input: {
    fontSize: 20,
    padding: 10,
    marginTop: 20,
  },
  title: {
    fontSize: 32,
  },
});
