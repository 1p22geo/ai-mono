import {StyleSheet, Text, View} from 'react-native';
import React from 'react';
import {MessageContext} from '../../types';

export const ContextView = ({context}: {context: MessageContext}) => {
  return (
    <>
      <View style={styles.context}>
        <Text style={styles.source}>{context.source}</Text>
        <Text style={styles.content}>{context.content}</Text>
      </View>
    </>
  );
};
const styles = StyleSheet.create({
  context: {
    display: 'flex',
    padding: 10,
    paddingLeft: 30,
  },
  source: {
    fontStyle: 'italic',
  },
  content: {
    fontSize: 20,
  },
});
