import React, { Fragment } from 'react';
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
      let response = await fetch('http://hackday.imp.sky.com/employee/getbyname', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({
              token: '772FDCDA27C4572D141E27B3E21E5',
              name: customFilterKey,
          }),
      });
      console.log(response)
      if (response.status == 200 ){
        let resp = await response.json();
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
//   if (!!customFilterKey) {
//     options = options.filter(option => new RegExp(`^.*?(${customFilterKey}).*?$`).test(option.label));
//   }
  if (options.length==0 && customFilterKey && customFilterKey.length>0) {
    options.push({
      label:"Not result found. Please try again!",
      value:false})
  }
  return new Promise(resolve => setTimeout(() => resolve(options), 1000));
};

const resolveFilters = () => ({
  a: 1,
});

const staticModalOptions = createStaticModalOptions();

const Employee = () => {
  let modalRef;
  const openModal = () => modalRef.show();
  const saveModalRef = ref => modalRef = ref;
  const onSelectedOption = value => {
    console.log(`You selected: ${value}`);
  };
  return (
    <Fragment>
      <SafeAreaView style={styles.container}>
        <Button title="Open Modal" onPress={openModal} />
      </SafeAreaView>
      <ModalSelectList
        ref={saveModalRef}
        placeholder={"Text something..."}
        closeButtonText={"Close"}
        // options={staticModalOptions}
        onSelectedOption={onSelectedOption}
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
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default Employee;