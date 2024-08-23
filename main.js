/* FORM SUBMITS */
document.querySelector('#emp-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const empFormData = JSON.stringify(
        Object.fromEntries(new FormData(document.querySelector('form#emp-form')))
    );
    console.log('emp data', empFormData);
    createEmployee(empFormData);
});

document.querySelector('#asset-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const assetFormData = JSON.stringify(
        Object.fromEntries(new FormData(document.querySelector('form#asset-form')))
    );
    console.log('asset data:', assetFormData)
    createAsset(empFormData);
});

/* CONSTANTS */
const employeeEndpoint = '/api/employees';
const assetEndpoint = '/api/assets';
const headers = {
    'Content-type': 'application/json'
};

/**
 * @TODO task list
 * 1. clean up forms on submit
 * 2. create UI tables for displaying employees and assets
 * 3. add update and delete UI functionality, passing in unique id
 * 4. clean up file, reduce repetetiveness of CRUD functions with shared helpers
 */

/* EMPLOYEE CRUD */
async function getEmployees() {
    const response = await fetch(employeeEndpoint);
    return response;
}

async function getEmployeeById(id) {
    const response = await fetch(`${employeeEndpoint}/${id}`);
    return response;
}

async function createEmployee(data) {
    const response = await fetch(employeeEndpoint, {
        method: 'POST',
        body: data,
        headers,
    });
    return response;
}

async function updateEmployee(data, id) {
    const response = await fetch(`${employeeEndpoint}/${id}`, {
        method: 'PUT',
        body: data,
        headers,
    });
    return response;
}

async function deleteEmployee(id) {
    const response = await fetch(`${employeeEndpoint}/${id}`, {
        method: 'DELETE',
    });
    return response;
}

/* ASSET CRUD */
async function getAssets() {
    const response = await fetch(assetEndpoint);
    return response;
}

async function getAssetById(id) {
    const response = await fetch(`${assetEndpoint}/${id}`);
    return response;
}

async function createAsset(data) {
    const response = await fetch(assetEndpoint, {
        method: 'POST',
        body: data,
        headers,
    });
    return response;
}

async function updateAsset(data, id) {
    const response = await fetch(`${assetEndpoint}/${id}`, {
        method: 'PUT',
        body: data,
        headers,
    });
    return response;
}

async function deleteAsset(id) {
    const response = await fetch(`${assetEndpoint}/${id}`, {
        method: 'DELETE',
    });
    return response;
}