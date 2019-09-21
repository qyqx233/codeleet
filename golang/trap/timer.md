1. 不要在循环内创建定时任务

```go
f+unc useNewTimer(in <-chan string) {
    defer wg.Done()
    idleDuration := 3 * time.Minute
    idleDelay := time.NewTimer(idleDuration)
    defer idleDelay.Stop()
 
    for Running {
        idleDelay.Reset(idleDuration)
 
        select {
        case _, ok := <-in:
            if !ok {
                return
            }
 
            // handle `s`
        case <-idleDelay.C:
            return
        }
    }
}
```