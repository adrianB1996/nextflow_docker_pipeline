project_dir = projectDir

process ProcessBAMandBED {
publishDir(path: '{$project_dir}/data/processeddata/processed', mode: 'copy', pattern: '*')
    """
    python $project_dir/bin/workflow.py --input_folder $project_dir/data/input --output_folder $project_dir/data/processed
    """
}

workflow{
  ProcessBAMandBED()
}