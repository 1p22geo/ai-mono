import React from 'react';
import {StyleSheet, View} from 'react-native';
import {Message} from '../types';
import {MessageView} from '../MessageView';

export const MessagesView = ({messages}: {messages: Message[]}) => (
  <>
    <View style={styles.list}>
      {messages.map((message, ix) => (
        <MessageView message={message} key={ix.toString()} />
      ))}
    </View>
  </>
);

const styles = StyleSheet.create({
  list: {
    marginTop: 10,
  },
});
