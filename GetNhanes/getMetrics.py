import os
import pandas as pd


def get_nhanes_data(years, features, basepath, metric_prefix,
                    output_dir=None, merge_output=False):
    """
    从NHANES数据集中提取并合并指定指标数据

    :param years: 需要处理的年份列表（例如 ['2007-2008', '2009-2010']）
    :param features: 需要提取的特征列（None表示所有列，必须包含'seqn'或文件包含'seqn'）
    :param basepath: NHANES数据存储的根目录
    :param metric_prefix: 目标指标的文件名前缀（如'DEET'）
    :param output_dir: 输出目录（默认为当前目录下的nhanes_output）
    :param merge_output: 是否合并所有文件（默认False）
    """
    # 参数校验
    if features is not None:
        if not features:  # 新增空列表检查
            raise ValueError("Features list cannot be empty.")
        if 'seqn' not in features:
            raise ValueError("Features must include 'seqn'.")
    if not os.path.exists(basepath):
        raise FileNotFoundError(f"Base path not found: {basepath}")
    if not years:
        raise ValueError("Years list cannot be empty.")

    # 设置输出目录
    output_dir = output_dir or os.path.join(os.getcwd(), "nhanes_output")
    os.makedirs(output_dir, exist_ok=True)

    # 计算年份范围
    def get_year_range(years):
        start_years = []
        end_years = []
        for y in years:
            parts = y.split('-')
            start = parts[0][:4]  # 处理类似2007-2008格式
            end = parts[-1][:4] if len(parts) > 1 else start
            start_years.append(start)
            end_years.append(end)
        return f"{min(start_years)}-{max(end_years)}"

    # 初始化数据存储
    all_data = []
    search_dirs = ["Laboratory", "Questionnaire", "Examination", "Dietary" ,"Demographics"]
    matched_files = []

    # 文件搜索阶段
    for year in years:
        for data_dir in search_dirs:
            current_path = os.path.join(basepath, year, data_dir, "tsv")
            if not os.path.isdir(current_path):
                continue

            try:
                files = [f for f in os.listdir(current_path)
                         if f.startswith(metric_prefix) and f.endswith(".tsv")]
                for f in files:
                    full_path = os.path.join(current_path, f)
                    matched_files.append((year, data_dir, full_path))
                    print(f"🔍 发现文件: {year}/{data_dir}/{f}")
            except Exception as e:
                print(f"⚠️ 扫描错误 {current_path}: {str(e)}")

    # 数据处理阶段
    for year, data_dir, file_path in matched_files:
        try:
            df = pd.read_csv(file_path, sep='\t', low_memory=False)

            # 列检查与选择
            if features is None:
                # 确保存在seqn列
                if 'seqn' not in df.columns:
                    print(f"⏩q 跳过 {os.path.basename(file_path)}，缺失列: seqn")
                    continue
                selected_columns = df.columns.tolist()
            else:
                # 检查指定列是否存在
                missing = [col for col in features if col not in df.columns]
                if missing:
                    print(f"⏩ 跳过 {os.path.basename(file_path)}，缺失列: {', '.join(missing)}")
                    continue
                selected_columns = features

            # 保存单个文件
            output_name = f"{year}_{data_dir}_{metric_prefix}.csv"
            single_path = os.path.join(output_dir, output_name)
            df[selected_columns].to_csv(single_path, index=False)
            print(f"💾 保存单个文件: {output_name} ({len(df)} 行)")

            # 为合并准备数据
            if merge_output:
                all_data.append(df[selected_columns])

        except Exception as e:
            print(f"❌ 处理失败 {file_path}: {str(e)}")

    # 合并处理
    if merge_output and all_data:
        merged_df = pd.concat(all_data, ignore_index=True)
        year_range = get_year_range(years)
        merged_name = f"{year_range}_{metric_prefix}.csv"
        merged_path = os.path.join(output_dir, merged_name)

        merged_df.to_csv(merged_path, index=False)
        print(f"✨ 合并完成！总数据量: {len(merged_df)} 行")
        print(f"📦 合并文件路径: {merged_path}")
    return True


if __name__ == '__main__':
    # 示例调用（保存所有列）
    get_nhanes_data(
        years=['1999-2000', '2001-2002', '2003-2004', '2005-2006',
               '2007-2008', '2009-2010', '2011-2012', '2013-2014',
               '2015-2016', '2017-2018', '2019-2020'],
        features=None,  # 不指定features，保存所有列
        basepath="E:\\NHANES_DATA\\2024-08-18完整版\\01_NHANES",
        metric_prefix="demo",
        merge_output=True
    )


