import React, { Fragment,PureComponent } from 'react';
import {
  SafeAreaView,
  StyleSheet,
  Button,
  AppRegistry,
} from 'react-native';
import {
  ModalSelectList,
} from 'react-native-modal-select-list';

console.disableYellowBox = true;

const createRandomString = (length = 10) => {
  var result           = '';
  var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  var charactersLength = characters.length;
  for ( var i = 0; i < length; i++ ) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
};

const createStaticModalOptions = () => {
  const options = [];
  for (let i = 0; i < 20; i++) {
    const word = createRandomString();
    options.push({ label: word, value: word });
  }
  return options;
};

const modalOptionsProvider = async ({ page, pageSize, customFilterKey }) => {
  let options = [];
  try {
    if (customFilterKey && customFilterKey.length>3){
      console.log("Sending Employee Request")
      let response = await fetch('http://hackday.imp.sky.com/employeegetbyname', {
          method: 'POST',
          cache: 'no-cache',
          headers: {
                'Content-Type': 'application/json'
          },
          body: JSON.stringify({
              token: '772FDCDA27C4572D141E27B3E21E5',
              name: customFilterKey,
          }),
      });
      if (response.status == 200 ){
        let resp = await response.json();
        console.log(resp)
        resp.body.employees.forEach((employee)=>{
            options.push(
              { 
                label: employee.cn, 
                value: employee
              }
            )
        })
      }
    }
  } catch (error) {
    // TODO: Modal alert box
    console.error(error);
  }
  // if (!!customFilterKey) {
  //   options = options.filter(option => new RegExp(`^.*?(${customFilterKey}).*?$`).test(option.label));
  // }
  // if (options.length==0 && customFilterKey && customFilterKey.length>0) {
  //   options.push({
  //     label:"Not result found. Please try again!",
  //     value:false})
  // }
  return new Promise(resolve => setTimeout(() => resolve(options), 1000));
};

const resolveFilters = () => ({
  a: 1,
});

const staticModalOptions = createStaticModalOptions();

class Employee extends PureComponent {

  constructor(navigation) {
    super();
    this.navigation = navigation
    this.params = navigation.route.params
    this.modalRef = React.createRef();
  }

  componentDidMount() {
    this.openModal()
  }

  openModal(){
    return this.modalRef.current.show()
  }

  onSelectedOption(value){
    let data = {
      employee: value,
      params: this.params
    }
    this.navigation.navigation.navigate('Confirmation',data)
//    console.log(data);
// {"employee": {"cn": "Martin, Frans", "email": "mar@sky.uk", "mobile": "+", "user": "pal"}, "params": {"base64": "/9j/4AAQSkZJRgABAQAAAQABAA...", "deviceOrientation": 1, "height": 300, "pictureOrientation": 1, "width": 400}}
  }

  render() {

    return (
      <Fragment>
        {/* <SafeAreaView style={styles.container}>
          <Button title="Open Modal" onPress={this.openModal.bind(this)} />
        </SafeAreaView> */}
        <ModalSelectList
          ref={this.modalRef}
          placeholder={"Enter employee name..."}
          closeButtonText={"Close"}
          // options={staticModalOptions}
          onSelectedOption={this.onSelectedOption.bind(this)}
          disableTextSearch={false}
          provider={modalOptionsProvider} 
          pageSize={40}
          inputName="customFilterKey"
          filter={resolveFilters}
          headerTintColor="purple"
          buttonTextColor="white"
        />
      </Fragment>
    );
  }
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default Employee;