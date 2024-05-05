import React, {useState} from 'react';
import {StyleSheet, Text, View} from 'react-native';
import {Message} from '../types';
import {ContextView} from './ContextView';

export const MessageView = ({message}: {message: Message}) => {
  const [show, setShow] = useState(false);
  return (
    <>
      <View style={styles.message}>
        <Text style={styles.author}>{message.author}:</Text>
        <Text style={styles.content}>{message.content}</Text>
        {message.context?.length ? (
          <Text style={styles.context} onPress={() => setShow(s => !s)}>
            ---- {!show ? 'open' : 'close'} context ( {message.context?.length}{' '}
            items ) ----
          </Text>
        ) : (
          <></>
        )}
        {show ? (
          message.context?.map((item, ix) => (
            <ContextView context={item} key={ix} />
          ))
        ) : (
          <></>
        )}
      </View>
    </>
  );
};
const styles = StyleSheet.create({
  message: {
    display: 'flex',
    padding: 10,
  },
  author: {
    fontStyle: 'italic',
  },
  context: {
    fontStyle: 'italic',
  },
  content: {
    fontSize: 20,
  },
});
