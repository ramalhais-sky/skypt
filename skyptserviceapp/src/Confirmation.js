import React, { Fragment,PureComponent } from 'react';
import { View, StyleSheet, Button, Text, Image, Modal, ToastAndroid } from 'react-native';
class Confirmation extends PureComponent {

  constructor(navigation) {
    super();
    this.navigation = navigation
    this.params = navigation.route.params
  }

  state = {
    modalVisible: false,
  };

  setModalVisible(visible) {
    this.setState({modalVisible: visible});
  }

  goHome(){
      console.log("goinghome")
      this.navigation.navigation.navigate("Home")
      this.setState({modalVisible: false});
  }

  async sendMessage(){ 
    try {
        let body = JSON.stringify({
                token: '772FDCDA27C4572D141E27B3E21E5',
                user: this.params.employee.user,
                package: `data:image/jpeg;base64,${this.params.params.base64}`
            })
        let payload = {
            method: 'POST',
            cache: 'no-cache',
            headers: {
                'Content-Type': 'application/json'
            },
            body: body
        };
        console.log("Sending Create Request",payload)
        let response = await fetch('http://hackday.imp.sky.com/packageadd',payload);
        console.log(response)
        if (response.status == 200 ){
            let resp = await response.json();
            this.params.packageID = resp.body.package
            // {"body": {"data": "Message sent", "mail": "S", "package": 287}, "statusCode": 200}
            console.log(resp)
            this.setModalVisible(true);
        } else {
            // TODO: Modal Alert Box
            ToastAndroid.show('Error packageAdd response!', ToastAndroid.SHORT);
        }
    } catch (error) {
        // TODO: Modal alert box
        console.error(error);
        ToastAndroid.show('Error packageAdd call!', ToastAndroid.SHORT);
    }
  }
 
  render() {
    return (
        <View style={styles.container}> 
            <Text style={styles.text}>{ this.params.employee.cn }</Text>
            <Text style={styles.text}>{ this.params.employee.email }</Text>
            <Text style={styles.text}>{ this.params.employee.mobile }</Text>
            <Image  style={[styles.image,{width:this.params.params.width,height:this.params.params.height}]}  source={{uri: `data:image/jpeg;base64,${this.params.params.base64}`}} />
            <Text style={styles.text}></Text>
            <Button style={styles.button} title="Send Package Alert" onPress={this.sendMessage.bind(this)}/>

            <Modal
            animationType="slide"
            transparent={false}
            visible={this.state.modalVisible}>
                <View  style={styles.container}>
                    <View>
                        <Text style={styles.text}>Message sent!</Text>
                        <Text style={styles.text}>ID:{this.params.packageID}</Text>
                        <Button style={styles.button} title="Close" onPress={this.goHome.bind(this)}/>
                    </View>
                </View>
            </Modal>

        </View>
    );
  }
};

const styles = StyleSheet.create({
  button: {
      paddingTop: 20
  },
  text: {
      fontSize: 18
  },
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  image: {
    padding: 5,
    resizeMode: 'contain'
  }
});

export default Confirmation;