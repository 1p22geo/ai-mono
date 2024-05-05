/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */

import React, {useState} from 'react';
import {
  Button,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  useColorScheme,
  View,
} from 'react-native';

import {Colors} from 'react-native/Libraries/NewAppScreen';
import {RagStore} from './RagStore';
import {Chat} from './Chat';
import {AppMode} from './utils';
import {Message} from './Chat/types';

function App(): React.JSX.Element {
  const [mode, setMode] = useState<AppMode>('chat');
  const isDarkMode = useColorScheme() === 'dark';
  const [messages, setMessages] = useState<Message[]>([]);

  const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  };

  return (
    <SafeAreaView style={backgroundStyle}>
      <StatusBar
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        backgroundColor={backgroundStyle.backgroundColor}
      />
      <ScrollView
        contentInsetAdjustmentBehavior="automatic"
        style={backgroundStyle}>
        <View>
          <View style={style.toggle}>
            <Button title="chat" onPress={() => setMode('chat')} />
            <Button title="store" onPress={() => setMode('store')} />
          </View>
          {(function () {
            switch (mode) {
              case 'chat':
                return <Chat messages={messages} setMessages={setMessages} />;
              case 'store':
                return <RagStore />;
            }
          })()}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

export default App;

const style = StyleSheet.create({
  toggle: {
    display: 'flex',
    flexDirection: 'row',
  },
});
