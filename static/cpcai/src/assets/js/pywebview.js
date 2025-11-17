export function getTaskStatus(refData) {
    
//     refData.value = [{ 'task_id': '89943af47698a71ccb630eb669e','env':'DEV02', 'database': { 'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_830' }, 'task_name': 'Test222', 'folder': 'Test222-2024-02-23 09-56-06', 'base_info': 'Test222-2024-02-23 09-56-06', 'sql': ' SELECT *\nFROM eclinical_subject_item esi\n         join eclinical_subject_crfversion esc on esi.subject_version_id = esc.id and esc.is_lastest = true', 'current': 999, 'total': 10000, 'state': 4, 'desc': 'Test222-2024-02-23 09-56-06 执行中' }
//     // { 'task_id': '5e84589943af47698a71ccb630eb669e','env':'DEV02', 'database': { 'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_830' }, 'task_name': 'Test222', 'folder': 'Test222-2024-02-23 09-56-06', 'base_info': 'Test222-2024-02-23 09-56-06', 'sql': ' SELECT *\nFROM eclinical_subject_item esi\n         join eclinical_subject_crfversion esc on esi.subject_version_id = esc.id and esc.is_lastest = true', 'current': 1000, 'total': 10000, 'state': 1, 'desc': 'Test222-2024-02-23 09-56-06 执行中' },
//     // { 'task_id': '5e84589943af47698a71ccb630eb669e', 'env':'DEV02','database': { 'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_830' }, 'task_name': 'Test222', 'folder': 'Test222-2024-02-23 09-56-06', 'base_info': 'Test222-2024-02-23 09-56-06', 'sql': ' SELECT *\nFROM eclinical_subject_item esi\n         join eclinical_subject_crfversion esc on esi.subject_version_id = esc.id and esc.is_lastest = true', 'current': 1000, 'total': 20000, 'state': 1, 'desc': 'Test222-2024-02-23 09-56-06 执行中' },
//     // {'task_id': '199148e1479146bd93ebf9af5adb7428', 'database': {'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_830'}, 'task_name': 'test01', 'folder': 'test01-2024-02-23 16-17-45', 'base_info': 'test01-2024-02-23 16-17-45', 'sql': 'SELECT * FROM eclinical_subject_visit', 'current': 20597, 'total': 20597, 'state': 4, 'desc': 'test01-2024-02-23 16-17-45 执行完毕', 'env': 'DEV01'}, {'task_id': 'c1adceb2ba504f278e29343b4a6ec674', 'database': {'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_899'}, 'task_name': 'jjj', 'folder': 'jjj-2024-02-23 16-18-44', 'base_info': 'jjj-2024-02-23 16-18-44', 'sql': 'SELECT * FROM eclinical_subject_visit', 'current': 26, 'total': 26, 'state': 4, 'desc': 'jjj-2024-02-23 16-18-44 执行完毕', 'env': 'DEV01'}, {'task_id': '834495247c4e4112b38b823a9dc36a61', 'database': {'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_830'}, 'task_name': 'kkkkkk', 'folder': 'kkkkkk-2024-02-23 16-19-08', 'base_info': 'kkkkkk-2024-02-23 16-19-08', 'sql': 'dadasdasd', 'current': 0, 'total': 0, 'state': -1, 'desc': '(1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'dadasdasd LIMIT 1000 OFFSET 0\' at line 1")', 'env': 'DEV01'}
// ];
    pywebview.api.getTaskStatus().then((result = []) => {
        refData.value = result;
    });
}

export function getDefault(schemaId,lifecycle, system,environment,taskName,sql, limit, year, month){
    pywebview.api.default().then((result) => {
        schemaId.value = result.schemaId
        lifecycle.value = result.lifecycle
        system.value = result.system
        environment.value = result.environment
        taskName.value = result.taskName
        sql.value = result.sql
        limit.value = result.limit;
        year.value = result.year
        month.value = result.month
    });
    console.log(year)
    console.log(month)
}


export function getEnvironmentOptions(refData) {
    pywebview.api.environmentOptions().then((result = []) => {
        console.log(result)
        refData.value = result;
    });
}

export function getSystemOptions(refData) {
    refData.value = [{'text': 'edc', 'value': 'edc'}, {'text': 'admin', 'value': 'admin'}, {'text': 'ctms', 'value': 'ctms'}, {'text': 'etmf', 'value': 'etmf'}, {'text': 'pv', 'value': 'pv'}, {'text': 'coding_company', 'value': 'coding_company'}, {'text': 'coding_study', 'value': 'coding_study'}, {'text': 'medical_coding', 'value': 'medical_coding'}, {'text': 'medical_coding_dictionary', 'value': 'medical_coding_dictionary'}, {'text': 'iwrs', 'value': 'iwrs'}, {'text': 'econsent', 'value': 'econsent'}]

    // pywebview.api.systemOptions().then((result = []) => {
    //     refData.value = result;
    // });
}

export function submitPyTask(env, system, lifeCycle, schemaId, taskName, sql, limit, year, month) {
    pywebview.api.submitTask(env.value, system.value, lifeCycle.value, schemaId.value, 
        taskName.value, sql.value, limit.value,
        year.value, month.value).then((result) => {
        console.log(taskName + "start")
    });
}

export function reSubmitPyTask(task_id){
    pywebview.api.resubmitTask(task_id).then((result) => {
        console.log("start")
    });
}

export function interruptPyTask(task_id){
    pywebview.api.interruptTask(task_id).then((result) => {
        console.log(task_id + "interrupted")
    });
}

export function getHistoryTasks(taskHistory, filterConds){
//     taskHistory.value = [{ 'task_id': '5e84589943a','env':'DEV01', 'database': { 'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_830' }, 'task_name': 'Test222', 'folder': 'Test222-2024-02-23 09-56-06', 'base_info': 'Test222-2024-02-23 09-56-06', 'sql': ' SELECT *\nFROM eclinical_subject_item esi\n         join eclinical_subject_crfversion esc on esi.subject_version_id = esc.id and esc.is_lastest = true', 'current': 999, 'total': 10000, 'state': 4, 'desc': 'Test222-2024-02-23 09-56-06 执行中' }
//     // { 'task_id': '5e84589943af47698a71ccb630eb669e','env':'DEV01', 'database': { 'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_830' }, 'task_name': 'Test222', 'folder': 'Test222-2024-02-23 09-56-06', 'base_info': 'Test222-2024-02-23 09-56-06', 'sql': ' SELECT *\nFROM eclinical_subject_item esi\n         join eclinical_subject_crfversion esc on esi.subject_version_id = esc.id and esc.is_lastest = true', 'current': 1000, 'total': 10000, 'state': 1, 'desc': 'Test222-2024-02-23 09-56-06 执行中' },
//     // { 'task_id': '5e84589943af47698a71ccb630eb669e', 'env':'DEV01','database': { 'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_830' }, 'task_name': 'Test222', 'folder': 'Test222-2024-02-23 09-56-06', 'base_info': 'Test222-2024-02-23 09-56-06', 'sql': ' SELECT *\nFROM eclinical_subject_item esi\n         join eclinical_subject_crfversion esc on esi.subject_version_id = esc.id and esc.is_lastest = true', 'current': 1000, 'total': 20000, 'state': 1, 'desc': 'Test222-2024-02-23 09-56-06 执行中' },
//     // {'task_id': '199148e1479146bd93ebf9af5adb7428', 'database': {'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_830'}, 'task_name': 'test01', 'folder': 'test01-2024-02-23 16-17-45', 'base_info': 'test01-2024-02-23 16-17-45', 'sql': 'SELECT * FROM eclinical_subject_visit', 'current': 20597, 'total': 20597, 'state': 4, 'desc': 'test01-2024-02-23 16-17-45 执行完毕', 'env': 'DEV01'}, {'task_id': 'c1adceb2ba504f278e29343b4a6ec674', 'database': {'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_899'}, 'task_name': 'jjj', 'folder': 'jjj-2024-02-23 16-18-44', 'base_info': 'jjj-2024-02-23 16-18-44', 'sql': 'SELECT * FROM eclinical_subject_visit', 'current': 26, 'total': 26, 'state': 4, 'desc': 'jjj-2024-02-23 16-18-44 执行完毕', 'env': 'DEV01'}, {'task_id': '834495247c4e4112b38b823a9dc36a61', 'database': {'host': 'dev-01.c9qe4y0vrvda.rds.cn-northwest-1.amazonaws.com.cn', 'user': 'root', 'password': '3fgRCcB72Px1FvBfDBNL', 'port': 3306, 'schema': 'eclinical_edc_dev_830'}, 'task_name': 'kkkkkk', 'folder': 'kkkkkk-2024-02-23 16-19-08', 'base_info': 'kkkkkk-2024-02-23 16-19-08', 'sql': 'dadasdasd', 'current': 0, 'total': 0, 'state': -1, 'desc': '(1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near \'dadasdasd LIMIT 1000 OFFSET 0\' at line 1")', 'env': 'DEV01'}
// ];
    pywebview.api.getHistoryTasks(filterConds.value).then((result) => {
        taskHistory.value = result
    });
}

export function deletePyTask(task_id){
    pywebview.api.remove_history(task_id).then((result) => {
        console.log(task_id + "deleted")
    });
}

export function getYears(years){
    pywebview.api.getYears().then((result) =>{
        years.value = result
        console.log(years.value)
    })
}
export const Event ="pywebviewready" // "DOMContentLoaded " //pywebviewready"
