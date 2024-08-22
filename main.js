document.querySelector('#submit-employee').addEventListener('click', createEmployee);
document.querySelector('#submit-asset').addEventListener('click', createAsset);

const empFormData = JSON.stringify(Object.fromEntries(new FormData(document.querySelector('form#emp-form'))));
const assetFormData = JSON.stringify(Object.fromEntries(new FormData(document.querySelector('form#emp-form'))));

function createEmployee(e) {
    e.preventDefault();
    console.log('hello employee');
}

function createAsset(e) {
    e.preventDefault();
    console.log('hello asset');
}