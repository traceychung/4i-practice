// handle form data
document.querySelector('#emp-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const empFormData = JSON.stringify(Object.fromEntries(new FormData(document.querySelector('form#emp-form'))));
    console.log('emp data', empFormData);
});

document.querySelector('#asset-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const assetFormData = JSON.stringify(Object.fromEntries(new FormData(document.querySelector('form#asset-form'))));
    console.log('asset data:', assetFormData)
});

// employee crud
function createEmployee(data) {
    // post
}

function updateEmployee(data) {
    // put
}

function deleteEmployee(data) {
    // delete
}

// asset crud
function createAsset(data) {
    // post
}
function updateAsset(data) {
    // post
}
function deleteAsset(data) {
    // delet
}