/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */

import React, { useCallback, useState } from 'react';
import {
  Button,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
} from 'react-native';

import { constants } from './constants';

import {
  Colors,
} from 'react-native/Libraries/NewAppScreen';


import DocumentPicker, { DocumentPickerResponse } from 'react-native-document-picker'


function App(): React.JSX.Element {
  const [fileResponse, setFileResponse] = useState<DocumentPickerResponse[]>([]);
  const [error, setError] = useState("")

  const handleDocumentSelection = useCallback(async () => {
    try {
      const response = await DocumentPicker.pick({
        allowMultiSelection: false,
        presentationStyle: 'fullScreen',
      });
      setFileResponse(response);
    } catch (err: any) {
      setError(err.toString())
    }
  }, []);

  const uploadFile = useCallback(async () => {
    try {
      let data = new FormData()
      data.append('file', { uri: fileResponse[0].uri, type: fileResponse[0].type, name: fileResponse[0].name })
      const response = await fetch(new URL("/upload", constants.ENDPOINT_URI), {
        method: 'POST',
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        body: data
      })
      throw "Uploaded"
    } catch (err: any) {
      setError(err.toString())
    }
  }, [fileResponse]);

  const isDarkMode = useColorScheme() === 'dark';

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
          <Text>
            {error || "No error yet."}
          </Text>
          <Button title="Select file"
            onPress={handleDocumentSelection}
          ></Button>
          {fileResponse.length == 1 ?
            <>
              <Text
                style={styles.highlight}
                numberOfLines={1}
                ellipsizeMode={'middle'}>
                Upload file:{fileResponse[0]?.name}
              </Text>
              <Button title="UPLOAD"
                onPress={uploadFile}
              ></Button>

            </> : <></>}
          {fileResponse.length > 1 ? <Text>
            Please upload just a single file!
          </Text> : <></>}

        </View>
      </ScrollView>
    </SafeAreaView >
  );
}

const styles = StyleSheet.create({
  highlight: {
    fontWeight: '700',
  },
});

export default App;
