import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useCallback } from 'react'

function ProblemListContainer() {
    const getProblems = useCallback(()=>{

        // const result = await fetch("abc").then(resp=>resp.json()).then(result=>result)
        
        return [

            {
                problem_id: Math.random(),
                problem_title: Math.random(),
            },{
                problem_id: Math.random(),
                problem_title: Math.random(),
            },{
                problem_id: Math.random(),
                problem_title: Math.random(),
            },{
                problem_id: Math.random(),
                problem_title: Math.random(),
            },{
                problem_id: Math.random(),
                problem_title: Math.random(),
            },{
                problem_id: Math.random(),
                problem_title: Math.random(),
            },{
                problem_id: Math.random(),
                problem_title: Math.random(),
            },{
                problem_id: Math.random(),
                problem_title: Math.random(),
            }
        ]
    }, [])
    const queryClient = useQueryClient()
    const { isPending, isError, data, error } = useQuery( {queryKey: ['problems'], queryFn: getProblems})

    const mutation = useMutation({
        mutationFn: postProblem,
        onSuccess: () => {
            queryClient.invalidateQueries( { queryKey: ['problems']} )
        },
    })

    return <div>

    </div>

}

export default ProblemListContainer
