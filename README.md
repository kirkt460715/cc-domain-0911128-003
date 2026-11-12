# 护理床位登记与供给审核

项目提供已有台账、领域计算、追溯与本地发布能力。主要业务边界见源代码中的输入契约，研究资料的字段和单位见[数据字典](数据字典.md)。所有示例和新增研究输入都是合成数据。

## 运行环境

Python 3.11 或更新版本；基础业务使用标准库与 SQLite。 依赖版本固定在仓库清单中，依赖准备完成后，测试和演示均可在本地运行，不需要账号或外部服务。计算较多的研究可使用清单中的 NumPy、SciPy；基础业务的运行路径保持独立。

```sh
python3 -m pip install -r requirements.txt
```

## 验证与演示

测试覆盖当前产品的核心操作、异常输入和恢复行为。编译检查与业务演示可分别执行；演示使用临时存储或随项目保存的合成资料。

```sh
python3 -m unittest discover -s tests -v
python3 -m compileall -q registry bed_events indicators audit bed_audit.py
python3 bed_audit.py demo --fixture fixtures/registry.json
```

## 目录与数据

业务模块：bed_events/timeline、bed_events/replay、indicators、audit/package。tests 保留产品回归，fixtures 保存可直接查看的本地业务资料。fixtures/study-input.json 与其数据字典独立登记研究输入，不覆盖原来的演示资料。

运行时产出的数据库、导出文件和研究结果请放在仓库外或 outputs 目录。修改输入应保留原始版本，公开数据需要沿用产品现有的披露边界。
